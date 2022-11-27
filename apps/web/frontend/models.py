from django.db import models


# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True
        get_latest_by = ("-updated_at", "-created_at",)
        ordering = ("-updated_at", "-created_at",)

    created_at = models.DateTimeField(verbose_name="新建时间", blank=True, null=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="编辑时间", blank=True, null=False, auto_now=True)
    deleted_at = models.DateTimeField(verbose_name="删除时间", blank=True, null=True)
    uuid = models.CharField(verbose_name="uuid", max_length=36, unique=True, blank=True, null=False)

    objects = models.Manager()


class Department(BaseModel):
    class Meta:
        db_table = "frontend_departments"

    name = models.CharField(verbose_name="部门名称", max_length=64, unique=True, blank=False, null=False)


class Account(BaseModel):
    class Meta:
        db_table = "frontend_accounts"
        order_with_respect_to = "department"

    username = models.CharField(verbose_name="账号", max_length=64, unique=True, blank=False, null=False)
    password = models.CharField(verbose_name="密码", max_length=128, blank=False, null=False)
    nickname = models.CharField(verbose_name="昵称", max_length=64, unique=True, blank=False, null=False)
    department = models.ForeignKey(
        verbose_name="所属部门",
        db_constraint=False,
        name="department_uuid",
        to="Department",
        to_field="uuid",
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        blank=True,
        related_name="accounts",
        related_query_name="accounts",
    )


class RbacRole(BaseModel):
    class Meta:
        db_table = "frontend_rbac_roles"

    name = models.CharField(verbose_name="角色名称", max_length=64, unique=True, blank=False, null=False)


class PivotRbacRoleAndAccount(BaseModel):
    class Meta:
        db_table = "frontend_pivot_rbac_role_and_accounts"

    rbac_role_uuid = models.CharField(verbose_name="所属角色uuid", max_length=36, blank=False, null=False)
    account_uuid = models.CharField(verbose_name="所属用户uuid", max_length=36, blank=False, null=False)
