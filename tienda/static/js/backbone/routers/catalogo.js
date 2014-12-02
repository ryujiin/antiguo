Loviz.Routers.Catalogo = Backbone.Router.extend({
	routes : {
		"catalogo/" : "catalogo",
		"producto/:slug/:id/" : 'producto_single',
		"catalogo/:slug/" : "catalogo",
		'lovizdc/:slug':'laucher',

	},
	initialize : function () {
  	},
	catalogo : function () {
		if (this.catalogo_creado === undefined ) {
			window.views.catalogo_contenedor.collection.fetch();

			if (this.filtros===undefined) {
				window.views.catalogo_contenedor.crear_filtros();
				this.filtros = true
			};
			if (this.cates === undefined ) {
				window.views.catalogo_contenedor.crear_categorias();
				this.cates = true;
			};
		    window.views.catalogo_contenedor.$('.filtros').empty();	
		    this.catalogo_creado = true;
		    debugger;
		};
		
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
	laucher:function (slug) {
	}
})