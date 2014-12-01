Loviz.Routers.Catalogo = Backbone.Router.extend({
	routes : {
		"catalogo/" : "catalogo",
		"producto/:slug/:id/" : 'producto_single',
	},
	initialize : function () {
  	},
	catalogo : function () {
		console.log('estamos en el catalogo ');
		window.views.catalogo_contenedor.collection.fetch();
		if (this.categorias===undefined) {
			var coleccion = new Loviz.Collections.Filtros();
			coleccion.filtro='Categoria';
			this.categorias = new Loviz.Views.CajaFiltros({
				collection : coleccion
			})
		}
	},
	crear_catalogo:function () {

	},
	producto_single:function (slug,id) {
		var modelo = new Loviz.Models.Producto({id:id});
		modelo.fetch().done(function () {
			if (window.views.producto_single) {
				var json = modelo.toJSON();
				window.views.producto_single.model.set(json);
			}else{
				window.views.producto_single = new Loviz.Views.ProductoSingle({
					model:modelo,
				});	
			}			
		});
	},
})