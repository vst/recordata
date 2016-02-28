import Ember from 'ember';

export default Ember.Controller.extend({
  /**
   * Defines the selected/new instance.
   */
  instance: null,

  /**
   * Defines errors if any.
   */
  errors: null,

  actions: {
    new: function () {
      this.transitionToRoute("records.detail", "new");
    },

    select: function (item) {
      this.transitionToRoute("records.detail", item.id);
    },
  }
});
