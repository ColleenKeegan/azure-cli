# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

STORAGE_RESOURCE_TYPE = 'Microsoft.Storage/storageAccounts'

ACR_RESOURCE_PROVIDER = 'Microsoft.ContainerRegistry'
REGISTRY_RESOURCE_TYPE = ACR_RESOURCE_PROVIDER + '/registries'
WEBHOOK_RESOURCE_TYPE = REGISTRY_RESOURCE_TYPE + '/webhooks'
REPLICATION_RESOURCE_TYPE = REGISTRY_RESOURCE_TYPE + '/replications'

TASK_RESOURCE_TYPE = REGISTRY_RESOURCE_TYPE + '/tasks'
TASK_VALID_VSTS_URLS = ['visualstudio.com', 'dev.azure.com']


def get_classic_sku(cmd):
    SkuName = cmd.get_models('SkuName')
    return [SkuName.classic.value]


def get_managed_sku(cmd):
    SkuName = cmd.get_models('SkuName')
    return [SkuName.basic.value, SkuName.standard.value, SkuName.premium.value]


def get_premium_sku(cmd):
    SkuName = cmd.get_models('SkuName')
    return [SkuName.premium.value]


def get_valid_os(cmd):
    OS = cmd.get_models('OS')
    return [item.value.lower() for item in OS]


def get_valid_architecture(cmd):
    Architecture = cmd.get_models('Architecture')
    return [item.value.lower() for item in Architecture]


def get_valid_variant(cmd):
    Variant = cmd.get_models('Variant')
    return [item.value.lower() for item in Variant]
