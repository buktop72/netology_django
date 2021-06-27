# TODO: опишите сериализаторы
from rest_framework import serializers

from measurements.models import Measurement, Project


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'
		# fields = 'id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at'


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = '__all__'
		# fields = 'id', 'value', 'project', 'created_at', 'updated_at'
