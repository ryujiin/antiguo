Loviz.Views.Tienda = Backbone.View.extend({
	events: {
<<<<<<< HEAD
		'click .link' : 'linknormal',
		'click .logo' : 'navega_home',
		'blur .requerido':'verificar_input_requerido',
		'blur input[type=password]':'verificar_pass',
		'blur input[type=email]':'verificar_email',
		'click .login_face' : 'login_face',
=======
		'click .link':'link_intero',
>>>>>>> loviz
	},
	initialize : function ($el) {
		var self = this;
		this.$el = $el;
	},
	link_intero:function (e) {
		e.preventDefault();
		var link = e.currentTarget.pathname;
		
		window.routers.base.navigate(link, {trigger:true});
<<<<<<< HEAD
	},
	obt_galleta : function(){
		var galleta = $.cookie('carrito');
		if (galleta==null) {
			console.log('veamos');
			var session = getRandomChar();
			$.cookie('carrito',session,{ expires: 1, path: '/'});
			galleta = session;
		};
		function getRandomChar() {
			numCara = 50
			chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
			pass ='';
			for (i=0;i<numCara;i++) {
				x = Math.floor(Math.random()*62);
				pass+=chars.charAt(x);
			};
			return pass
		};
		return galleta
	},
	verificar_input_requerido:function (e) {
		var div = $(e.currentTarget);
		var valor = div.val();
		var texto_ayuda;
		if (valor ==='') {
			texto_ayuda = '<span class="icon-cross2">Este campo es obligatorio*'
			this.inputError(div,texto_ayuda);
		}
	},
	verificar_pass:function (e) {
		var div = $(e.currentTarget);
		var valor = div.val();
		var texto_ayuda;
		var lonitud = valor.length;
		if (valor!=='') {
			if (lonitud<5) {
				texto_ayuda = '<span class="icon-cross2">La contraseña no puede ser menor de 5 caracteres'
				this.inputError(div,texto_ayuda)
				div.val('');
			}else{
				div.addClass('bueno')
				div.next().empty();	
			}
		};
	},
	verificar_email:function (e) {
		var div = $(e.currentTarget);
		var valor = div.val();
		var texto_ayuda;
		var email = this.validarEmail(valor)
		if (valor!=='') {
			if (email===false) {
				texto_ayuda = '<span class="icon-cross2">Porfavor ingrese un Correo Valido'
				this.inputError(div,texto_ayuda)
				div.val('');
			}else{
				div.addClass('bueno')
				div.next().empty();
			}
		};				
	},
	inputError:function (div,texto_ayuda) {
		div.removeClass('bueno');
		div.addClass('fallo');
		contedor = div.next();
		contedor.empty().addClass('text_fallo').append(texto_ayuda);
	},
	validarEmail:function( email ) {
		expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		if ( !expr.test(email) ){
		 	return false
		}else{
		 	return true
		}
	},
	modificar_cabezera:function (titulo,descripcion) {
		document.title=titulo + ' | LovizdelCarpio.com'
		$('meta[name="description"]').remove();
		$('head').append("<meta name='description' content='"+descripcion+"'>");
=======
>>>>>>> loviz
	}
});
