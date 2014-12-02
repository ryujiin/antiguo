Loviz.Views.Catalogo_contenedor = Backbone.View.extend({
	el:$('#catalogo'),
	events: {
	},
	initialize : function () {
		var self = this;

		window.routers.catalogo.on('route',function(e){
			self.aparecer(e);
		});
		window.routers.base.on('route',function(e){
			self.aparecer(e);
		});
	},
	render:function () {
		if (this.collection.length===0) {
	    	this.listenTo(this.collection, "add", this.addOne, this);
		};
    	this.collection.forEach(this.addOne, this);
	},
	aparecer:function (e) {
		if (e === 'catalogo') {
			this.$el.show();
		}else{
			this.$el.hide();
		}
	},
	addOne: function (produ) {
		var producto = new Loviz.Views.ProductoLista({ model: produ });
		this.$('.productos').append(producto.render().el);
	},
	crear_categorias:function  () {
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