from django.db import models
from typing import Type
from abc import abstractmethod


class IDHandler:
    @abstractmethod
    def is_valid(self, update_params, model_instance, class_name, defined_exception: Type[Exception]):
        if update_params.get("id") and update_params.get("id") != model_instance.id:
            raise defined_exception(
                f'The {class_name}.id {model_instance.id} is not equal to model instance {update_params.get("id")}.'
            )


class TimeModel(models.Model, IDHandler):
    id: int
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_id(self) -> int:
        return self.id
