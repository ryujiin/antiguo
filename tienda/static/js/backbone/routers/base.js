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
		this.views_carro = new Loviz.Views.Carro();
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