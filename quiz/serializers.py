from rest_framework import serializers
from .models import Banner, User, Instruction, Content


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['content']

class InstructionSerializer(serializers.ModelSerializer):
    contents = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    contents_output = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Instruction
        fields = ['id', 'page', 'title', 'contents', 'contents_output']

    def get_contents_output(self, obj):
        return [c.content for c in obj.contents.all()]

    def create(self, validated_data):
        contents_data = validated_data.pop('contents', [])
        instruction = Instruction.objects.create(**validated_data)
        for content_text in contents_data:
            Content.objects.create(ins_title=instruction, content=content_text)
        return instruction

    def to_representation(self, instance):
        """Rename output key 'contents_output' → 'contents'"""
        representation = super().to_representation(instance)
        representation['contents'] = representation.pop('contents_output')
        return representation





class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'
        # fields = [
        #     "id",
        #     "title_english", "subtitle_english", "button_english",
        #     "title_bangla", "subtitle_bangla", "button_bangla", "page", "image", "is_active", 'created_at'
        # ]
        # # Bangla fields are auto-generated — return them but don't require the client to send them
        # read_only_fields = [
        #     "title_bangla", "subtitle_bangla", "button_bangla", "created_at"
        # ]





    

