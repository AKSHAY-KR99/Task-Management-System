from rest_framework import serializers

from tasks.models import CustomUser, Task


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "role"]


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    assigned_by = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "due_date",
            "created_at",
            "updated_at",
            "assigned_to",
            "assigned_by",
            "completion_report",
            "worked_hours",
        ]

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["status", "worked_hours", "completion_report"]

    def validate(self, data):
        task = self.instance

        if task.status not in ["pending", "in_progress"]:
            raise serializers.ValidationError("Only pending or in-progress tasks can be updated.")

        if data.get("status") == "completed":
            if not data.get("worked_hours") or not data.get("completion_report"):
                raise serializers.ValidationError(
                    "Worked Hours and Completion Report are required when marking task as completed."
                )

        return data
