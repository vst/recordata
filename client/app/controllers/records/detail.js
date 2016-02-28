import Ember from 'ember';

export default Ember.Controller.extend({
  /**
   * Defines errors if any.
   */
  errors: null,

  actions: {
    save: function () {
      // Set errors to none:
      this.set("errors", null);

      // Attempt to save the instance:
      this.get("model").save().then(() => {
        // Notify the user:
        this.notifications.success("Saved!");

        // Route back to the listing:
        this.transitionToRoute("records");
      }).catch((error) => {
        // Notify the user:
        this.notifications.error("Problem while saving...");

        // Save errors:
        this.set("errors", error.errors);
      });
    },

    cancel: function () {
      // Set errors to none:
      this.set("errors", null);

      // Rollback attributes (or remove if it is new):
      this.get("model").rollbackAttributes();

      // Route back to the listing:
      this.transitionToRoute("records");
    },

    delete: function () {
      // Set errors to none:
      this.set("errors", null);

      // Rollback attributes (or remove if it is new):
      this.get("model").destroyRecord().then(() => {
        // Route back to the listing:
        this.transitionToRoute("records");
      });
    }
  }
});
