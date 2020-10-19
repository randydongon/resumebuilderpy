from rest_framework import serializers
from RandyApp.models import TypesOfResume, Profile


class TypesOfResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesOfResume
        fields = ('ResumeId',
                  'ResumeName')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'ProfileId',
            'Position',
            'AboutYourSelf',
            'FirstName',
            'LastName',
            'MiddleName',
            'BirthPlace',
            'PersonAdd',
            'Gender',
            'Nationality',
            'BirthDate',
            'BobileNumber',
            'EmailAdd',
            'ProSkills',
            'Elementary',
            'YearElemFrom',
            'YearElemTo',
            'AddressElem',
            'Secondary',
            'YearSecFrom',
            'YearSecTo',
            'AddressSec',
            'College',
            'YearColFrom',
            'YearColTo',
            'AddressCollege',
            'PhotoFileName',
            'CompanyName',
            'YearFromA',
            'YearToA',
            'AddressA',
            'DutiesA',
            'CompanyB',
            'YearFromB',
            'YearToB',
            'AddressB',
            'DutiesB',
            'CompanyC',
            'YearFromC',
            'YearToC',
            'AddressC',
            'DutiesC',
        )
