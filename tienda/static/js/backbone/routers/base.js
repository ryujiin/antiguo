Loviz.Routers.Base = Backbone.Router.extend({
	routes : {
		"" : "root",
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
	},
	pagar:function () {
		if (window.models.carro.toJSON().id!==undefined) {
		}else{
			this.navigate('/', {trigger:true});			
		}
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
	}
})