import Ember from "ember";


export default Ember.Route.extend({
  model: function (params) {
    if (params.id == "new") {
      return this.store.createRecord("record");
    }
    return this.store.find("record", params.id);
  },

  renderTemplate: function() {
    this.render("records/detail", {
      into: "application"
    });
  }
});
