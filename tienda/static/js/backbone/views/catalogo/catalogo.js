Loviz.Views.Catalogo_contenedor = Backbone.View.extend({
	el:$('#catalogo'),
	events: {
	},
	initialize : function () {
		var self = this;
    	
    	this.listenTo(this.collection, "add", this.addOne, this);

		window.routers.catalogo.on('route',function(e){
			self.aparecer(e);
		});
		window.routers.base.on('route',function(e){
			self.aparecer(e);
		});
	},
	aparecer:function (e) {
		if (e === 'catalogo' || e ==='categoria_catalogo') {
			this.$el.show();
			console.log(e)
		}else{
			this.$el.hide();
		}
	},
	addOne: function (produ) {
		var producto = new Loviz.Views.ProductoLista({ model: produ });
		this.$('.productos').append(producto.render().el);
	},
	crear_categorias:function  () {
		
		/*
		if (this.categorias===undefined) {
			debugger;
			var coleccion = new Loviz.Collections.Filtros();
			coleccion.filtro='Categoria';
			if (this.para_mujer===undefined) {
				this.para_mujer = new Loviz.Views.Cate_CajaFiltros({
					collection : coleccion,
				});
				this.para_mujer.genero='Mujeres';	
			};
			if (this.para_hombre===undefined) {
				this.para_hombre = new Loviz.Views.Cate_CajaFiltros({
					collection : coleccion,
				});
				this.para_hombre.genero='Hombres';		
			};
			if (this.kids===undefined) {
				this.kids = new Loviz.Views.Cate_CajaFiltros({
					collection : coleccion,
				});
				this.kids.genero="kid's";			
			};
			this.para_mujer.render();
			this.para_hombre.render();
			this.kids.render();
			coleccion.fetch();
			this.categorias = true;
			debugger;
		};
		*/
	},
	crear_filtros : function () {		
		if (this.estilos=== undefined) {
			var coleccion = new Loviz.Collections.Filtros();
			coleccion.filtro='Estilos';
			this.estilos = new Loviz.Views.CajaFiltros({
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
});