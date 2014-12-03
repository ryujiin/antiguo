Loviz.Views.Carro = Backbone.View.extend({
	el:$('#carro'),
	template : swig.compile($("#carro_template").html()),

	events :{
	},
	initialize: function () {
		var self = this;
		window.routers.base.on('route',function(e){
			self.borrar(e);
		});
	},
	render:function () {
		var html = this.template();
	    this.$el.html(html);
	},
	borrar:function (e) {
		if (e!=='carro') {
			this.$el.empty();
		};
	}
});