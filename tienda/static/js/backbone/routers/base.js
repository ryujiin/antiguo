Loviz.Routers.Base = Backbone.Router.extend({
	routes : {
		"" : "root",
		'ld/:slug/':'landing',		
		'carro/':'carro',
		'pagar/':'pagar',
		'ingresar/':'ingresar',
		'perfil/':'perfil',
		'*notFound': 'notFound',
	},
	initialize : function () {
  	},
	root : function () {
		window.app.state = "inicio";
		var titulo_web = 'Loviz DelCarpio :: lovizdelcarpio.com donde encontras los mejores pantuflas, botas, sandalias';
		var descriocion_web = 'Loviz DelCarpio® , Encontraras lo mejor en pantuflas, sandalias, botas, flats y demas. Envio Gratis para todo el peru por compras mayores a S/.60.00';
		window.views.tienda.modificar_cabezera(titulo_web,descriocion_web)
	},
	notFound:function () {
		console.log('no hay pagina')
	},
	carro:function () {
		if (window.views.carro===undefined) {
			window.views.carro = new Loviz.Views.Carro({
				collection: window.collections.lineas,
			});	
		}
		var titulo_web = 'Carrito de compras | LovizdelCarpio.com'
		var descriocion_web = 'El carrito de compras de LovizDelcarpio.com. compra con confianza'
		window.views.tienda.modificar_cabezera(titulo_web,descriocion_web)

	},
	pagar:function () {
		if (window.models.carro.toJSON().id!==undefined) {
		}else{
			this.navigate('/', {trigger:true});			
		}
		var titulo_web = 'Pagar | LovizdelCarpio.com'
		var descriocion_web = 'El carrito de compras de LovizDelcarpio.com. compra con confianza'
		window.views.tienda.modificar_cabezera(titulo_web,descriocion_web)
	},
	ingresar:function () {
		if (window.views.ingresar===undefined) {
			window.views.ingresar = new Loviz.Views.Ingresar();
		};
	},
	perfil:function () {
		if (window.views.perfil===undefined) {
			window.views.perfil = new Loviz.Views.Perfil({
				model:window.models.usuario,
			})	
		};		
	},
	pagar:function () {
		if (window.views.pagar===undefined) {
			window.views.pagar = new Loviz.Views.Pagar()
		}
	},
	landing:function (slug) {
		window.app.state='Landing';
		window.app.landing = slug;
		this.view_landing = new Loviz.Views.Landing();
	}
})