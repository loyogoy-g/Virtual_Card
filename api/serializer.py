from rest_framework import serializers
from .models import Student, FirstQuarter, SecondQuarter, ThirdQuarter, FourthQuarter

class FirstQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstQuarter
        fields =['Subject', 'Grade']

class SecondQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondQuarter
        fields =['Subject', 'Grade']

class ThirdQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdQuarter
        fields =['Subject', 'Grade']

class FourthQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FourthQuarter
        fields =['Subject', 'Grade']

class StudentSerializer(serializers.ModelSerializer):
    firstgrade = FirstQuarterSerializer(many=True)
    secondgrade = SecondQuarterSerializer(many=True)
    thirdgrade = ThirdQuarterSerializer(many=True)
    fourthgrade = FourthQuarterSerializer(many=True)
    class Meta:
        model = Student
        fields =["Name", "LRN", "Status", "Section", "Quarter", "firstgrade","secondgrade","thirdgrade","fourthgrade"]
        depth = 1

    def create(self, validated_data):
        firstquarter = validated_data.pop('firstgrade')
        validated_data.pop("secondgrade")
        validated_data.pop("thirdgrade")
        validated_data.pop("fourthgrade")
        student = Student.objects.create(**validated_data)
        for grade in firstquarter:
            FirstQuarter.objects.create(Student=student, **grade)
        return student