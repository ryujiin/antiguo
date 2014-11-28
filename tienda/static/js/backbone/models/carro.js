Loviz.Models.Carro = Backbone.Model.extend({
	urlRoot : '/api/carro/',
	name : 'Carro',
    url : function() {
        var base = this.urlRoot;
        if (this.isNew()) return base;
        return base + (base.charAt(base.length - 1) == '/' ? '' : '/') + this.id+'/';
    },
	initialize : function () {
        this.buscar_carro();
        this.listenTo(window.models.usuario, "change", this.buscar_carro, this);
	},
    defaults:{
        "propietario": null, 
        "estado": "Abierto", 
        "sesion_carro": "", 
        "lineas": 0, 
        "total": "0.00", 
        "subtotal": "0.00", 
        "envio": 0
    },
	buscar_carro:function () {
        var self = this;
        var usuario = window.models.usuario.toJSON().id
        if (usuario>0) {
            this.fetch().fail(function () {
                self.set('propietario',usuario);
            });
        }else{
            this.fetch({
                data:$.param({session:galleta})
            }).fail(function () {
                self.set('sesion_carro',galleta)
            })
        }
    },
    fucionar_carro:function(){
    	if (window.models.carro !== this) {
            if (this.toJSON().lineas !==0 ) {
                var self = this;
                var nueva_collecion = new Loviz.Collections.Lineas();
                nueva_collecion.fetch({
                    data:$.param({carro:this.id})
                })
                .done(function () {
                    nueva_collecion.forEach(function (linea) {
                        linea.set('carro',window.models.carro.id);
                        linea.save();
                    });
                    self.set('estado','Fusionada');
                    self.save().done(function () {
                        window.models.carro.set('propietario',usuario)
                        window.models.carro.save();
                    });                    
                });
            }else{
                window.models.carro.set({'propietario':usuario,'estado':'Abierto'});
                this.set('estado','Fusionada');
                this.save().done(function () {
                    window.models.carro.save();
                });
            }
    	};
    },
});