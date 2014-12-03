Loviz.Views.Carro = Backbone.View.extend({
	el:$('#carro'),
	template : swig.compile($("#carro_template").html()),
	events :{
	},
	initialize: function () {
		var self = this;
		this.render();
	},
	render:function () {
		var html = this.template();
	    this.$el.html(html);
	},
})