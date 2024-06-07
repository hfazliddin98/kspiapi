from rest_framework.serializers import ModelSerializer
from .models import Rektorat, Fakultet, Kafedra, Bolim, Markaz
from .models import RektoratRahbar, FakultetRahbar, KafedraRahbar, BolimRahbar, MarkazRahbar
from .models import RektoratHodim, FakultetHodim, KafedraHodim, BolimHodim, MarkazHodim



class RektoratSerializer(ModelSerializer):
    class Meta:
        model = Rektorat
        fields = '__all__'
        

class FakultetSerializer(ModelSerializer):
    class Meta:
        model = Fakultet
        fields = '__all__'
        

class KafedraSerializer(ModelSerializer):
    class Meta:
        model = Kafedra
        fields = '__all__'
        

class BolimSerializer(ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'
        

class MarkazSerializer(ModelSerializer):
    class Meta:
        model = Markaz
        fields = '__all__'

class RektoratRahbarSerializer(ModelSerializer):
    class Meta:
        model = RektoratRahbar
        fields = '__all__'
        

class FakultetRahbarSerializer(ModelSerializer):
    class Meta:
        model = FakultetRahbar
        fields = '__all__'
        

class KafedraRahbarSerializer(ModelSerializer):
    class Meta:
        model = KafedraRahbar
        fields = '__all__'
        

class BolimRahbarSerializer(ModelSerializer):
    class Meta:
        model = BolimRahbar
        fields = '__all__'
        

class MarkazRahbarSerializer(ModelSerializer):
    class Meta:
        model = MarkazRahbar
        fields = '__all__'

# Hodimlar

class RektoratHodimSerializer(ModelSerializer):
    class Meta:
        model = RektoratHodim
        fields = '__all__'
        

class FakultetHodimSerializer(ModelSerializer):
    class Meta:
        model = FakultetHodim
        fields = '__all__'
        

class KafedraHodimSerializer(ModelSerializer):
    class Meta:
        model = KafedraHodim
        fields = '__all__'
        

class BolimHodimSerializer(ModelSerializer):
    class Meta:
        model = BolimHodim
        fields = '__all__'
        

class MarkazHodimSerializer(ModelSerializer):
    class Meta:
        model = MarkazHodim
        fields = '__all__'
        



