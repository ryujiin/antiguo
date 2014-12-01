Loviz.Collections.Filtros = Backbone.Collection.extend({
	model : Loviz.Models.Filtro,
	name : 'Caja Filtro',
	url : function () {
		if (this.filtro==='Categoria') {
			return '/api/categorias/';
		};
	}
});