Loviz.Routers.Base = Backbone.Router.extend({
	routes : {
		"" : "root",
		'carro/':'carro',
		'pagina/:slug/':'pagina',
		'user/:slug/':'usuario',
		'catalogo/:slug/':'catalogo',
		'producto/:slug/':'producto',
		'*notFound': 'notFound',
	},
	initialize : function () {
  	},
	root : function () {
		window.app.state = "inicio";
	},
	carro : function () {
		if (this.views_carro===undefined) {
			this.views_carro = new Loviz.Views.Carro();
		};
		this.views_carro.render();
	},
	pagina: function () {
	},
	usuario : function () {
	},
	catalogo : function () {
	},
	producto : function () {
	},
	notFound:function () {
		console.log('no hay pagina')
	},
})