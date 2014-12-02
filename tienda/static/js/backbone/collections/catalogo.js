Loviz.Collections.Catalogo = Backbone.Collection.extend({
	model : Loviz.Models.ProductoLista,
	url : '/api/catalogo/',
	name : 'Catalogo',
	initialize : function () {
		this.fetch();
  	},
});