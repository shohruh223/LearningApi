from django.db.models import Model, DateTimeField, BooleanField, TextField


class BaseModel(Model):
    create_at = DateTimeField(auto_now_add=True)
    update_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DescriptionBaseModel(BaseModel):
    text = TextField(null=True, blank=True)

    class Meta:
        abstract = True


class DeletedModel(Model):
    deleted_at = DateTimeField(null=True, blank=True)
    is_deleted = BooleanField(default=False)

    class Meta:
        abstract = True



