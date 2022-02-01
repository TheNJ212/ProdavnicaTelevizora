from django import forms

IZBOR_BROJA_TELEVIZORA = [(i, str(i)) for i in range(1, 11)]


class FormaZaDodavanjeTelevizoraUKorpu(forms.Form):
    kolicina = forms.TypedChoiceField(choices=IZBOR_BROJA_TELEVIZORA,
                                      empty_value=1, coerce=int)  # prebaci u int
    dodati_na_kolicinu = forms.BooleanField(required=False, initial=True,
                                            widget=forms.HiddenInput)
