from rest_framework.serializers import ModelSerializer

from issue.models import Issue


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"

    def create(self, validated_data):
        return Issue(**validated_data)