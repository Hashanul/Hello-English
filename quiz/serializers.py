from rest_framework import serializers
from .models import Banner, User, Instruction, Content
from deep_translator import GoogleTranslator  # for automatic translation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'





class InstructionSerializer(serializers.ModelSerializer):
    contents_en = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=True
    )
    contents_bn = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    # Read-only output
    contents_en_output = serializers.SerializerMethodField(read_only=True)
    contents_bn_output = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Instruction
        fields = [
            'id',
            'page_en',
            'title_en',
            'page_bn',
            'title_bn',
            'contents_en',
            'contents_bn',
            'contents_en_output',
            'contents_bn_output',
        ]

    # Output methods
    def get_contents_en_output(self, obj):
        return [c.content_en for c in obj.contents.all()]

    def get_contents_bn_output(self, obj):
        return [c.content_bn for c in obj.contents.all()]

    # Create
    def create(self, validated_data):
        contents_en = validated_data.pop('contents_en', [])
        contents_bn = validated_data.pop('contents_bn', [])

        # Auto-translate if contents_bn is empty
        if not contents_bn:
            contents_bn = [GoogleTranslator(source='en', target='bn').translate(text) for text in contents_en]

        instruction = Instruction.objects.create(**validated_data)

        for en, bn in zip(contents_en, contents_bn):
            Content.objects.create(
                ins_title_en=instruction,
                content_en=en,
                content_bn=bn
            )

        return instruction

    # Update
    def update(self, instance, validated_data):
        contents_en = validated_data.pop('contents_en', None)
        contents_bn = validated_data.pop('contents_bn', None)

        # update instruction fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # update contents
        if contents_en is not None:
            instance.contents.all().delete()
            if not contents_bn:
                contents_bn = [GoogleTranslator(source='en', target='bn').translate(text) for text in contents_en]

            for en, bn in zip(contents_en, contents_bn):
                Content.objects.create(
                    ins_title_en=instance,
                    content_en=en,
                    content_bn=bn
                )

        return instance

    # Rename output fields
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['contents_en'] = rep.pop('contents_en_output')
        rep['contents_bn'] = rep.pop('contents_bn_output')
        return rep





class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
