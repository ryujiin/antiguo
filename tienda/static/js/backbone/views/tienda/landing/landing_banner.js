Loviz.Views.Landing_Banner_cate = Backbone.View.extend({
    className: 'banner',
    events: {
    },
    template: swig.compile($("#banner_categoria_template").html()),
    
    initialize: function () {
    },
    
    render: function () {
        var album = this.model.toJSON()
        var html = this.template(album);
        this.$el.html(html);
        return this;
    },
});