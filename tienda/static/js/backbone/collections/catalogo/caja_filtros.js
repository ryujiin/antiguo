Loviz.Collections.Filtros = Backbone.Collection.extend({
	model : Loviz.Models.Filtro,
	name : 'Caja Filtro',
	url : function () {
		if (this.filtro==='Categoria') {
			return '/api/categorias/';
		}else if(this.filtro === 'Genero'){
			return '/api/generos/'
		}else if (this.filtro==='Colores') {
			return '/api/colores/'
		}else if(this.filtro==='Estilos'){
			return '/api/estilos/'
		}
	}
});