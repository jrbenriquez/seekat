from rest_framework.serializers import ModelSerializer

class SESerializer(ModelSerializer):
    class Meta:
        nested_dynamic_fields = []

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally

        dynamic_field_param = kwargs.pop('nested_dynamic_param', '')
        super().__init__(*args, **kwargs)

        # https://medium.com/@Joelhanson25/advanced-serializer-usage-dynamically-modifying-fields-e7c3bc28efa6
        # Don't pass the 'fields' arg up to the superclass

        context = self.context

        request = context.get('request')
        # Nested Dynamic Fields
        # This happens in the parent serializer
        # We pass the "upper serializer" context to the "nested one"
        if hasattr(self.Meta, 'nested_dynamic_fields'):
            for field in self.Meta.nested_dynamic_fields:
                str_nested_fields = request.GET.get(field, '')
                nested_fields = str_nested_fields.split(',') if str_nested_fields else None
                if nested_fields:
                    allowed = set(nested_fields)
                    existing = set(self.fields[field].fields)
                    for nested_field in existing - allowed:
                        self.fields[field].fields.pop(nested_field)

        # Base Dynamic Fields
        str_fields = request.GET.get(dynamic_field_param, '') if request else None
        fields = str_fields.split(',') if str_fields else None
        if fields is not None:
            # Drop any fields that are not specified in the `fields`
            # argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

