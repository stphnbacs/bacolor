from django.forms import ModelForm
from .models import Group, Musician, Album, Track, Organizer, Contract, MusicianContractStatus

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = '__all__'

class OrganizerForm(ModelForm):
    class Meta:
        model = Organizer
        fields = '__all__'

class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

class MusicianContractStatusForm(ModelForm):
    class Meta:
        model = MusicianContractStatus
        fields = '__all__'
