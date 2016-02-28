import DS from 'ember-data';

export default DS.Model.extend({
  /**
   * Provides the key of the model.
   */
  key: DS.attr("string"),

  /**
   * Provides the value of the model.
   */
  value: DS.attr("string"),
});
