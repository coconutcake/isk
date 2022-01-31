from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

import func.functions as fnc
import func.generators as gen
import map.models
from django.core.exceptions import ValidationError, FieldError

class DepartmentCase(TestCase):
    """
    Map test class
    """

    def setUp(self) -> None:

        self.model = map.models.Department
        self.user = fnc.create_user(**gen.user_payload_gen().__next__())
        self.instances_fields = fnc.get_model_payload_instances_fields(
            self.model_obj_payload_gen().__next__()
        )

    def model_obj_payload_gen(self):
        """
        Generates various model object payloads (must to be customized!)
        """

        while True:

            string_gen = gen.custom_string_gen(
                big_letters=True, digits=True, gen_range=[5, 16]
                )

            payload = {
                "name": string_gen.__next__(),
                "description": string_gen.__next__()
                }

            yield payload

    def test_if_created_success(self):
        """
        Tests if model is created providing minimal proper data
        """

        p_gen = self.model_obj_payload_gen()
        payload_0 = p_gen.__next__()
        created = self.model.objects.create(**payload_0)

        created_with_instances = fnc.model_to_dict_with_instances(
            instance=created, fields=payload_0, instance_fields=self.instances_fields
        )

        self.assertTrue(created)
        self.assertEqual(created_with_instances, payload_0)

    def test_if_updated_success(self):
        """ 
        Tests if object is updated 
        """

        p_gen = self.model_obj_payload_gen()
        payload_0 = p_gen.__next__()
        payload_1 = p_gen.__next__()
        created = self.model.objects.create(**payload_0)

        self.model.objects.filter(pk=created.pk).update(**payload_1)

        updated = self.model.objects.get(pk=created.pk)

        updated_with_instances = fnc.model_to_dict_with_instances(
            instance=updated, fields=payload_0, instance_fields=self.instances_fields
        )

        self.assertEqual(updated_with_instances, payload_1)

    def test_if_deleted_success(self):
        """
        Tests if deleted
        """

        p_gen = self.model_obj_payload_gen()
        payload_0 = p_gen.__next__()
        created = self.model.objects.create(**payload_0)

        created_with_instances = fnc.model_to_dict_with_instances(
            instance=created, fields=payload_0, instance_fields=self.instances_fields
        )

        self.assertTrue(created)
        self.assertEqual(created_with_instances, payload_0)

        self.model.objects.filter(pk=created.id).delete()

        self.assertFalse(self.model.objects.filter(pk=created.pk).exists())




