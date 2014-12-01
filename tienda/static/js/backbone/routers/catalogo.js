Loviz.Routers.Catalogo = Backbone.Router.extend({
	routes : {
		"catalogo/" : "catalogo",
		"producto/:slug/:id/" : 'producto_single',
		"catalogo/:slug/" : "catalogo",

	},
	initialize : function () {
  	},
	catalogo : function (slug) {
		console.log('estamos en el catalogo ');
		window.views.catalogo_contenedor.collection.fetch();
		if (this.categorias===undefined) {
			var coleccion = new Loviz.Collections.Filtros();
			coleccion.filtro='Categoria';
			coleccion.cate = true;
			this.categorias = new Loviz.Views.CajaFiltros({
				collection : coleccion
			});
		};
		if (this.generos=== undefined) {
			var coleccion = new Loviz.Collections.Filtros();
			coleccion.filtro='Genero';
			this.generos = new Loviz.Views.CajaFiltros({
				collection : coleccion
			});
		};
		if (this.colores=== undefined) {
			var coleccion = new Loviz.Collections.Filtros();
			coleccion.filtro='Colores';
			this.colores = new Loviz.Views.CajaFiltros({
				collection : coleccion
			});
		};
		if (this.precios === undefined) {
			var coleccion = new Loviz.Collections.Filtro_precio();
			coleccion.filtro = 'Precios'
			this.precios = new Loviz.Views.CajaFiltros({
				collection : coleccion
			});
			this.addFiltro_precio(coleccion);
		};
		if (slug) {
			console.log('enrique')
		};
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
	addFiltro_precio:function (coleccion) {
		coleccion.add([
			{nombre : 'S/.20.00 y menores', slug : 'menor_20'},
			{nombre : 'S/.30.00 y menores', slug : 'menor_30'},
			{nombre : 'S/.40.00 y menores', slug : 'menor_40'},
			{nombre : 'S/.50.00 y menores', slug : 'menor_50'},
			{nombre : 'S/.50.00 y mayores', slug : 'mayor_50'},
		]);
	},
})