Loviz.Collections.Categorias = Backbone.Collection.extend({
	model : Loviz.Models.Filtro,
	url : '/api/categorias/',
	name : 'Categorias',
	initialize : function () {
		this.fetch();
  	},
});