Loviz.Collections.Catalogo = Backbone.Collection.extend({
	model : Loviz.Models.Producto,
	url : '/api/catalogo/',
	name : 'Catalogo',
});