from rest_framework import serializers

from black_clover.grimorios.models import Grimorio, Profile


class ProfileSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="get_gender_display")
    social_status = serializers.CharField(source="get_social_status_display")
    magical_affinity = serializers.CharField(source="get_magical_affinity_display")

    class Meta:
        model = Profile
        fields = "__all__"


class GrimorioSerializer(serializers.ModelSerializer):
    cover = serializers.CharField(source="get_cover_display")
    profile = ProfileSerializer()

    class Meta:
        model = Grimorio
        fields = "__all__"
        depth = 1
