# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots["test_api_list[ACLViewSet] 1"] = {
    "queries": [
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl"',
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user" WHERE "core_user"."id" IN (\'04adb4e2-f055-c978-c9bb-101ee1bc5cd4\'::uuid, \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid, \'ea416ed0-759d-46a8-de58-f63a59077499\'::uuid, \'f94c84fa-c5cb-091c-60bb-143cb957d229\'::uuid)',
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."id" IN (\'0b0cfc07-fca8-1c95-6ab9-181d8576f4a8\'::uuid, \'336311a0-1618-4326-ddbd-d61edd4eeb52\'::uuid, \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid, \'de59bd90-61c9-3855-e3fd-d416e26f27a6\'::uuid, \'df7c0a3f-a598-0975-2be3-92c52c4a0559\'::uuid, \'fb0e22c7-9ac7-5679-e988-1e6ba183b354\'::uuid)',
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" WHERE "core_role"."slug" IN (\'example-never-form\', \'fish-eat-just\', \'he-new-marriage\', \'impact-tend\', \'industry-call\', \'political-young\') ORDER BY "core_role"."slug" ASC',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'industry-call\'',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" = \'ea416ed0-759d-46a8-de58-f63a59077499\'::uuid',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'fb0e22c7-9ac7-5679-e988-1e6ba183b354\'::uuid',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'fish-eat-just\'',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" = \'04adb4e2-f055-c978-c9bb-101ee1bc5cd4\'::uuid',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'0b0cfc07-fca8-1c95-6ab9-181d8576f4a8\'::uuid',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'political-young\'',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'336311a0-1618-4326-ddbd-d61edd4eeb52\'::uuid',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'example-never-form\'',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" = \'f94c84fa-c5cb-091c-60bb-143cb957d229\'::uuid',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'df7c0a3f-a598-0975-2be3-92c52c4a0559\'::uuid',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'impact-tend\'',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'de59bd90-61c9-3855-e3fd-d416e26f27a6\'::uuid',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'he-new-marriage\'',
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/acls",
        "QUERY_STRING": "include=user%2Cscope%2Crole",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "industry-call", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "dad3a37a-a9d5-0688-b515-7698acfd7aee",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "fish-eat-just", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "fb0e22c7-9ac7-5679-e988-1e6ba183b354",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "ea416ed0-759d-46a8-de58-f63a59077499",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "aba369f7-d2b2-8a90-98a0-a26feb7dc965",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "political-young", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "0b0cfc07-fca8-1c95-6ab9-181d8576f4a8",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "04adb4e2-f055-c978-c9bb-101ee1bc5cd4",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "dcb740b2-c283-6cb1-1f70-7d63e6ac664f",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "example-never-form", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "336311a0-1618-4326-ddbd-d61edd4eeb52",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "04adb4e2-f055-c978-c9bb-101ee1bc5cd4",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "4e619f5b-28df-4a97-4496-3e6700abe7ca",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "impact-tend", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "df7c0a3f-a598-0975-2be3-92c52c4a0559",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "f94c84fa-c5cb-091c-60bb-143cb957d229",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "45ed9cc2-f92b-77cd-8b2f-5bd59ff635f8",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "he-new-marriage", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "de59bd90-61c9-3855-e3fd-d416e26f27a6",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "f94c84fa-c5cb-091c-60bb-143cb957d229",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
        ],
        "included": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Itself close again affect ok window church. Claim interview participant call strategy. Watch nor under window relate raise gun. Base hear human high word.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Scott Davis", "fr": ""},
                    "slug": "example-never-form",
                },
                "id": "example-never-form",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Wear wide even material. Pull require list usually.
Us value artist difficult make. Sport site lead base much American nice. Identify without nation reduce kitchen bit.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Catherine Matthews", "fr": ""},
                    "slug": "fish-eat-just",
                },
                "id": "fish-eat-just",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Though maintain work picture mother. Sell performance rule method sit as guy. Plan expert car hundred as interesting southern.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Robin Martin", "fr": ""},
                    "slug": "he-new-marriage",
                },
                "id": "he-new-marriage",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Tax ready cold across late performance dark. Hand affect cold traditional work able former everybody. Human hold talk manager west through argue culture. Community camera few trial.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Lori Murphy", "fr": ""},
                    "slug": "impact-tend",
                },
                "id": "impact-tend",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Of themselves garden weight table same method work. Mean finally realize us movie. Truth deep public these.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "David Benson", "fr": ""},
                    "slug": "industry-call",
                },
                "id": "industry-call",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Political heart outside capital direction capital Congress. Notice range laugh whether reduce.
Check official care or conference break. Remain daughter single.
For brother weight upon.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Mary Cook", "fr": ""},
                    "slug": "political-young",
                },
                "id": "political-young",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Find white continue none president. Idea eye plan third program. Article including take idea.
Officer player possible issue ahead suffer. Standard remember after away control expert without assume.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Jeffrey Zhang", "fr": ""},
                },
                "id": "0b0cfc07-fca8-1c95-6ab9-181d8576f4a8",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "aba369f7-d2b2-8a90-98a0-a26feb7dc965",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Role serious visit all truth change ok. Agency season worry take value eye sell. He consumer same season natural think Mr.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Jason Cisneros", "fr": ""},
                },
                "id": "336311a0-1618-4326-ddbd-d61edd4eeb52",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "dcb740b2-c283-6cb1-1f70-7d63e6ac664f",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Line whatever team suggest traditional boy. Drop argue move. Anyone remember prove.
Kid avoid player relationship to range whose. Draw free property consider.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Jessica Holloway", "fr": ""},
                },
                "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Service memory great. Career world town source spring somebody. Tonight yard prepare similar sense listen.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Donna Cain", "fr": ""},
                },
                "id": "de59bd90-61c9-3855-e3fd-d416e26f27a6",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "45ed9cc2-f92b-77cd-8b2f-5bd59ff635f8",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Cold relate right will avoid. Sense center mouth human great region.
Bar rate threat buy open should.
Decision cause although strong thing vote rate cost. And east hour.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Scott Doyle", "fr": ""},
                },
                "id": "df7c0a3f-a598-0975-2be3-92c52c4a0559",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "4e619f5b-28df-4a97-4496-3e6700abe7ca",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Final activity hope star check record well. Radio with Mr letter eye.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Diane Butler", "fr": ""},
                },
                "id": "fb0e22c7-9ac7-5679-e988-1e6ba183b354",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "dad3a37a-a9d5-0688-b515-7698acfd7aee",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "brownkatherine@example.com",
                    "first-name": "Heather",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Marsh",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "michaelkatherine",
                    "zip": None,
                },
                "id": "04adb4e2-f055-c978-c9bb-101ee1bc5cd4",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "aba369f7-d2b2-8a90-98a0-a26feb7dc965",
                                "type": "acls",
                            },
                            {
                                "id": "dcb740b2-c283-6cb1-1f70-7d63e6ac664f",
                                "type": "acls",
                            },
                        ],
                        "meta": {"count": 2},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "banderson@example.com",
                    "first-name": "Amanda",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Gallagher",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "mark48",
                    "zip": None,
                },
                "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "foleysarah@example.org",
                    "first-name": "Brandon",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Bartlett",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "rosscynthia",
                    "zip": None,
                },
                "id": "ea416ed0-759d-46a8-de58-f63a59077499",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "dad3a37a-a9d5-0688-b515-7698acfd7aee",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "tmcbride@example.net",
                    "first-name": "Karen",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Shaw",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "amandakaufman",
                    "zip": None,
                },
                "id": "f94c84fa-c5cb-091c-60bb-143cb957d229",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "4e619f5b-28df-4a97-4496-3e6700abe7ca",
                                "type": "acls",
                            },
                            {
                                "id": "45ed9cc2-f92b-77cd-8b2f-5bd59ff635f8",
                                "type": "acls",
                            },
                        ],
                        "meta": {"count": 2},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
        ],
    },
    "status": 200,
}

snapshots["test_api_list[PermissionViewSet] 1"] = {
    "queries": [
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission"'
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/permissions",
        "QUERY_STRING": "include=",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Bit among again across environment long line. Team suggest traditional boy above.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Jordan Mccarthy", "fr": ""},
                    "slug": "mrs-shake-recent",
                },
                "id": "mrs-shake-recent",
                "relationships": {"created-by-user": {"data": None}},
                "type": "permissions",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Size lead run then project find white. Those player foreign idea. Area media increase meeting article.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Angela Brown", "fr": ""},
                    "slug": "reason-son-current",
                },
                "id": "reason-son-current",
                "relationships": {"created-by-user": {"data": None}},
                "type": "permissions",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Wide happy air represent. Cup debate medical. Today morning standard effort summer.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Justin Hunt", "fr": ""},
                    "slug": "structure",
                },
                "id": "structure",
                "relationships": {"created-by-user": {"data": None}},
                "type": "permissions",
            },
        ]
    },
    "status": 200,
}

snapshots["test_api_list[RoleViewSet] 1"] = {
    "queries": [
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" ORDER BY "core_role"."slug" ASC',
        'SELECT ("core_role_permissions"."role_id") AS "_prefetch_related_val_role_id", "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" IN (\'mrs-shake-recent\', \'reason-son-current\', \'structure\', \'tree-ground-history\')',
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/roles",
        "QUERY_STRING": "include=permissions",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Bit among again across environment long line. Team suggest traditional boy above.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Jordan Mccarthy", "fr": ""},
                    "slug": "mrs-shake-recent",
                },
                "id": "mrs-shake-recent",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {
                        "data": [{"id": "rather-cost-admit", "type": "permissions"}],
                        "meta": {"count": 1},
                    },
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Size lead run then project find white. Those player foreign idea. Area media increase meeting article.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Angela Brown", "fr": ""},
                    "slug": "reason-son-current",
                },
                "id": "reason-son-current",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Wide happy air represent. Cup debate medical. Today morning standard effort summer.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Justin Hunt", "fr": ""},
                    "slug": "structure",
                },
                "id": "structure",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Material police pull require list usually large exactly. Value artist difficult make listen unit seven lead.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Brandy Jones", "fr": ""},
                    "slug": "tree-ground-history",
                },
                "id": "tree-ground-history",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
        ],
        "included": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Thing for east later still. Number inside put fire try cell.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Courtney Brewer", "fr": ""},
                    "slug": "rather-cost-admit",
                },
                "id": "rather-cost-admit",
                "relationships": {"created-by-user": {"data": None}},
                "type": "permissions",
            }
        ],
    },
    "status": 200,
}

snapshots["test_api_list[ScopeViewSet] 1"] = {
    "queries": [
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" ORDER BY "core_scope"."tree_id" ASC, "core_scope"."lft" ASC',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid, \'dad3a37a-a9d5-0688-b515-7698acfd7aee\'::uuid, \'f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad\'::uuid, \'fb0e22c7-9ac7-5679-e988-1e6ba183b354\'::uuid)',
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/scopes",
        "QUERY_STRING": "include=acls",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Effort meet relationship far. Option program interesting station. First where during teach country talk across.
Argue move appear catch toward help wind. Material minute ago get.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Pamela Horton", "fr": ""},
                },
                "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                "relationships": {
                    "acls": {"data": [], "meta": {"count": 0}},
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Environmental statement bag someone them style. Exactly follow spring view mind. Tax final upon stay sing middle suggest.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Trevor Castaneda", "fr": ""},
                },
                "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "ea416ed0-759d-46a8-de58-f63a59077499",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Bank arm serious live by itself. Project find white continue none president. Idea eye plan third program.
Son success provide beyond. Officer player possible issue ahead suffer.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Rebecca Gonzalez", "fr": ""},
                },
                "id": "fb0e22c7-9ac7-5679-e988-1e6ba183b354",
                "relationships": {
                    "acls": {"data": [], "meta": {"count": 0}},
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Free environment measure role later now over.
Can bed notice range. Minute can second prove every check official. Stay culture create risk.
Daughter single product trade.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Lorraine Reynolds", "fr": ""},
                },
                "id": "dad3a37a-a9d5-0688-b515-7698acfd7aee",
                "relationships": {
                    "acls": {"data": [], "meta": {"count": 0}},
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
        ],
        "included": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "ea416ed0-759d-46a8-de58-f63a59077499",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "piece-example", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            }
        ],
    },
    "status": 200,
}

snapshots["test_api_list[UserViewSet] 1"] = {
    "queries": [
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user"',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" IN (\'04adb4e2-f055-c978-c9bb-101ee1bc5cd4\'::uuid, \'336311a0-1618-4326-ddbd-d61edd4eeb52\'::uuid, \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid, \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/users",
        "QUERY_STRING": "include=acls",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": [
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "ssanchez@example.org",
                    "first-name": "Elizabeth",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Coleman",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "qguerra",
                    "zip": None,
                },
                "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "ea416ed0-759d-46a8-de58-f63a59077499",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "banderson@example.com",
                    "first-name": "Amanda",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Gallagher",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "mark48",
                    "zip": None,
                },
                "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "dad3a37a-a9d5-0688-b515-7698acfd7aee",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "brownkatherine@example.com",
                    "first-name": "Heather",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Marsh",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "michaelkatherine",
                    "zip": None,
                },
                "id": "04adb4e2-f055-c978-c9bb-101ee1bc5cd4",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "aba369f7-d2b2-8a90-98a0-a26feb7dc965",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "katherine02@example.net",
                    "first-name": "Mark",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Barnes",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "xnixon",
                    "zip": None,
                },
                "id": "336311a0-1618-4326-ddbd-d61edd4eeb52",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "f94c84fa-c5cb-091c-60bb-143cb957d229",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
        ],
        "included": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "aba369f7-d2b2-8a90-98a0-a26feb7dc965",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "political-young", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "0b0cfc07-fca8-1c95-6ab9-181d8576f4a8",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "04adb4e2-f055-c978-c9bb-101ee1bc5cd4",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "dad3a37a-a9d5-0688-b515-7698acfd7aee",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "explain-first", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "fb0e22c7-9ac7-5679-e988-1e6ba183b354",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "ea416ed0-759d-46a8-de58-f63a59077499",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "deep-public-these", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "f94c84fa-c5cb-091c-60bb-143cb957d229",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "nearly-food-skill", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "dcb740b2-c283-6cb1-1f70-7d63e6ac664f",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "336311a0-1618-4326-ddbd-d61edd4eeb52",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            },
        ],
    },
    "status": 200,
}

snapshots["test_api_detail[ACLViewSet] 1"] = {
    "queries": [
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."id" = \'f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad\'::uuid',
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user" WHERE "core_user"."id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."id" IN (\'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid)',
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" WHERE "core_role"."slug" IN (\'industry-call\') ORDER BY "core_role"."slug" ASC',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'industry-call\'',
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/acls/f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
        "QUERY_STRING": "include=user%2Cscope%2Crole",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "modified-at": "2017-05-21T00:00:00Z",
            },
            "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
            "relationships": {
                "created-by-user": {"data": None},
                "role": {"data": {"id": "industry-call", "type": "roles"}},
                "scope": {
                    "data": {
                        "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                        "type": "scopes",
                    }
                },
                "user": {
                    "data": {
                        "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                        "type": "users",
                    }
                },
            },
            "type": "acls",
        },
        "included": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Of themselves garden weight table same method work. Mean finally realize us movie. Truth deep public these.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "David Benson", "fr": ""},
                    "slug": "industry-call",
                },
                "id": "industry-call",
                "relationships": {
                    "created-by-user": {"data": None},
                    "permissions": {"data": [], "meta": {"count": 0}},
                },
                "type": "roles",
            },
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": """Line whatever team suggest traditional boy. Drop argue move. Anyone remember prove.
Kid avoid player relationship to range whose. Draw free property consider.""",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Jessica Holloway", "fr": ""},
                },
                "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                    "parent": {"data": None},
                },
                "type": "scopes",
            },
            {
                "attributes": {
                    "address": None,
                    "city": None,
                    "created-at": "2017-05-21T00:00:00Z",
                    "date-joined": "2017-05-21T00:00:00Z",
                    "email": "banderson@example.com",
                    "first-name": "Amanda",
                    "is-active": True,
                    "language": "en",
                    "last-name": "Gallagher",
                    "meta": {},
                    "modified-at": "2017-05-21T00:00:00Z",
                    "phone": None,
                    "username": "mark48",
                    "zip": None,
                },
                "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                "relationships": {
                    "acls": {
                        "data": [
                            {
                                "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
                                "type": "acls",
                            }
                        ],
                        "meta": {"count": 1},
                    },
                    "created-by-user": {"data": None},
                },
                "type": "users",
            },
        ],
    },
    "status": 200,
}

snapshots["test_api_detail[PermissionViewSet] 1"] = {
    "queries": [
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" WHERE "core_permission"."slug" = \'mrs-shake-recent\''
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/permissions/mrs-shake-recent",
        "QUERY_STRING": "include=",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": "Bit among again across environment long line. Team suggest traditional boy above.",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Jordan Mccarthy", "fr": ""},
                "slug": "mrs-shake-recent",
            },
            "id": "mrs-shake-recent",
            "relationships": {"created-by-user": {"data": None}},
            "type": "permissions",
        }
    },
    "status": 200,
}

snapshots["test_api_detail[RoleViewSet] 1"] = {
    "queries": [
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" WHERE "core_role"."slug" = \'mrs-shake-recent\'',
        'SELECT ("core_role_permissions"."role_id") AS "_prefetch_related_val_role_id", "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" IN (\'mrs-shake-recent\')',
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/roles/mrs-shake-recent",
        "QUERY_STRING": "include=permissions",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": "Bit among again across environment long line. Team suggest traditional boy above.",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Jordan Mccarthy", "fr": ""},
                "slug": "mrs-shake-recent",
            },
            "id": "mrs-shake-recent",
            "relationships": {
                "created-by-user": {"data": None},
                "permissions": {
                    "data": [{"id": "rather-cost-admit", "type": "permissions"}],
                    "meta": {"count": 1},
                },
            },
            "type": "roles",
        },
        "included": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "description": {
                        "de": "",
                        "en": "Thing for east later still. Number inside put fire try cell.",
                        "fr": "",
                    },
                    "modified-at": "2017-05-21T00:00:00Z",
                    "name": {"de": "", "en": "Courtney Brewer", "fr": ""},
                    "slug": "rather-cost-admit",
                },
                "id": "rather-cost-admit",
                "relationships": {"created-by-user": {"data": None}},
                "type": "permissions",
            }
        ],
    },
    "status": 200,
}

snapshots["test_api_detail[ScopeViewSet] 1"] = {
    "queries": [
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/scopes/9dd4e461-268c-8034-f5c8-564e155c67a6",
        "QUERY_STRING": "include=acls",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": """Effort meet relationship far. Option program interesting station. First where during teach country talk across.
Argue move appear catch toward help wind. Material minute ago get.""",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Pamela Horton", "fr": ""},
            },
            "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
            "relationships": {
                "acls": {"data": [], "meta": {"count": 0}},
                "created-by-user": {"data": None},
                "parent": {"data": None},
            },
            "type": "scopes",
        }
    },
    "status": 200,
}

snapshots["test_api_detail[UserViewSet] 1"] = {
    "queries": [
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user" WHERE "core_user"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
    ],
    "request": {
        "CONTENT_TYPE": "application/octet-stream",
        "PATH_INFO": "/api/v1/users/9dd4e461-268c-8034-f5c8-564e155c67a6",
        "QUERY_STRING": "include=acls",
        "REQUEST_METHOD": "GET",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "address": None,
                "city": None,
                "created-at": "2017-05-21T00:00:00Z",
                "date-joined": "2017-05-21T00:00:00Z",
                "email": "banderson@example.com",
                "first-name": "Amanda",
                "is-active": True,
                "language": "en",
                "last-name": "Gallagher",
                "meta": {},
                "modified-at": "2017-05-21T00:00:00Z",
                "phone": None,
                "username": "mark48",
                "zip": None,
            },
            "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
            "relationships": {
                "acls": {
                    "data": [
                        {"id": "dad3a37a-a9d5-0688-b515-7698acfd7aee", "type": "acls"}
                    ],
                    "meta": {"count": 1},
                },
                "created-by-user": {"data": None},
            },
            "type": "users",
        },
        "included": [
            {
                "attributes": {
                    "created-at": "2017-05-21T00:00:00Z",
                    "modified-at": "2017-05-21T00:00:00Z",
                },
                "id": "dad3a37a-a9d5-0688-b515-7698acfd7aee",
                "relationships": {
                    "created-by-user": {"data": None},
                    "role": {"data": {"id": "explain-first", "type": "roles"}},
                    "scope": {
                        "data": {
                            "id": "fb0e22c7-9ac7-5679-e988-1e6ba183b354",
                            "type": "scopes",
                        }
                    },
                    "user": {
                        "data": {
                            "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                            "type": "users",
                        }
                    },
                },
                "type": "acls",
            }
        ],
    },
    "status": 200,
}

snapshots["test_api_create[ACLViewSet] 1"] = {
    "queries": [
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user" WHERE "core_user"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."id" = \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid',
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" WHERE "core_role"."slug" = \'industry-call\'',
        'SELECT (1) AS "a" FROM "core_acl" WHERE ("core_acl"."role_id" = \'industry-call\' AND "core_acl"."scope_id" = \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid AND "core_acl"."user_id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)  LIMIT 1',
        'INSERT INTO "core_acl" ("created_at", "modified_at", "created_by_user_id", "id", "user_id", "scope_id", "role_id") VALUES (\'2017-05-21T00:00:00+00:00\'::timestamptz, \'2017-05-21T00:00:00+00:00\'::timestamptz, NULL, \'04adb4e2-f055-c978-c9bb-101ee1bc5cd4\'::uuid, \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid, \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid, \'industry-call\')',
    ],
    "request": {
        "CONTENT_LENGTH": "416",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/acls",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "POST",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "modified-at": "2017-05-21T00:00:00Z",
            },
            "id": "04adb4e2-f055-c978-c9bb-101ee1bc5cd4",
            "relationships": {
                "created-by-user": {"data": None},
                "role": {"data": {"id": "industry-call", "type": "roles"}},
                "scope": {
                    "data": {
                        "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                        "type": "scopes",
                    }
                },
                "user": {
                    "data": {
                        "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                        "type": "users",
                    }
                },
            },
            "type": "acls",
        }
    },
    "status": 201,
}

snapshots["test_api_create[PermissionViewSet] 1"] = {
    "queries": [
        'SELECT (1) AS "a" FROM "core_permission" WHERE "core_permission"."slug" = \'mrs-shake-recent\'  LIMIT 1',
        "INSERT INTO \"core_permission\" (\"created_at\", \"modified_at\", \"created_by_user_id\", \"slug\", \"name\", \"description\") VALUES ('2017-05-21T00:00:00+00:00'::timestamptz, '2017-05-21T00:00:00+00:00'::timestamptz, NULL, 'mrs-shake-recent', hstore(ARRAY['en','de','fr'], ARRAY['Jordan Mccarthy','','']), hstore(ARRAY['en','de','fr'], ARRAY['Bit among again across environment long line. Team suggest traditional boy above.','','']))",
    ],
    "request": {
        "CONTENT_LENGTH": "388",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/permissions",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "POST",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": "Bit among again across environment long line. Team suggest traditional boy above.",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Jordan Mccarthy", "fr": ""},
                "slug": "mrs-shake-recent",
            },
            "id": "mrs-shake-recent",
            "relationships": {"created-by-user": {"data": None}},
            "type": "permissions",
        }
    },
    "status": 201,
}

snapshots["test_api_create[RoleViewSet] 1"] = {
    "queries": [
        'SELECT (1) AS "a" FROM "core_role" WHERE "core_role"."slug" = \'mrs-shake-recent\'  LIMIT 1',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" WHERE "core_permission"."slug" = \'rather-cost-admit\'',
        "INSERT INTO \"core_role\" (\"created_at\", \"modified_at\", \"created_by_user_id\", \"slug\", \"name\", \"description\") VALUES ('2017-05-21T00:00:00+00:00'::timestamptz, '2017-05-21T00:00:00+00:00'::timestamptz, NULL, 'mrs-shake-recent', hstore(ARRAY['en','de','fr'], ARRAY['Jordan Mccarthy','','']), hstore(ARRAY['en','de','fr'], ARRAY['Bit among again across environment long line. Team suggest traditional boy above.','','']))",
        'SELECT "core_permission"."slug" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'mrs-shake-recent\'',
        'SELECT "core_role_permissions"."permission_id" FROM "core_role_permissions" WHERE ("core_role_permissions"."permission_id" IN (\'rather-cost-admit\') AND "core_role_permissions"."role_id" = \'mrs-shake-recent\')',
        'INSERT INTO "core_role_permissions" ("role_id", "permission_id") VALUES (\'mrs-shake-recent\', \'rather-cost-admit\') RETURNING "core_role_permissions"."id"',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'mrs-shake-recent\'',
    ],
    "request": {
        "CONTENT_LENGTH": "474",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/roles",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "POST",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": "Bit among again across environment long line. Team suggest traditional boy above.",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Jordan Mccarthy", "fr": ""},
                "slug": "mrs-shake-recent",
            },
            "id": "mrs-shake-recent",
            "relationships": {
                "created-by-user": {"data": None},
                "permissions": {
                    "data": [{"id": "rather-cost-admit", "type": "permissions"}],
                    "meta": {"count": 1},
                },
            },
            "type": "roles",
        }
    },
    "status": 201,
}

snapshots["test_api_create[ScopeViewSet] 1"] = {
    "queries": [
        'SELECT MAX("core_scope"."tree_id") AS "tree_id__max" FROM "core_scope"',
        """INSERT INTO "core_scope" ("created_at", "modified_at", "created_by_user_id", "id", "name", "description", "parent_id", "lft", "rght", "tree_id", "level") VALUES (\'2017-05-21T00:00:00+00:00\'::timestamptz, \'2017-05-21T00:00:00+00:00\'::timestamptz, NULL, \'fb0e22c7-9ac7-5679-e988-1e6ba183b354\'::uuid, hstore(ARRAY[\'en\',\'de\',\'fr\'], ARRAY[\'Pamela Horton\',\'\',\'\']), hstore(ARRAY[\'en\',\'de\',\'fr\'], ARRAY[\'Effort meet relationship far. Option program interesting station. First where during teach country talk across.
Argue move appear catch toward help wind. Material minute ago get.','','']), NULL, 1, 2, 3, 0)""",
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'fb0e22c7-9ac7-5679-e988-1e6ba183b354\'::uuid',
    ],
    "request": {
        "CONTENT_LENGTH": "534",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/scopes",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "POST",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": """Effort meet relationship far. Option program interesting station. First where during teach country talk across.
Argue move appear catch toward help wind. Material minute ago get.""",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Pamela Horton", "fr": ""},
            },
            "id": "fb0e22c7-9ac7-5679-e988-1e6ba183b354",
            "relationships": {
                "acls": {"data": [], "meta": {"count": 0}},
                "created-by-user": {"data": None},
                "parent": {"data": None},
            },
            "type": "scopes",
        }
    },
    "status": 201,
}

snapshots["test_api_create[UserViewSet] 1"] = {
    "queries": [
        'SELECT (1) AS "a" FROM "core_user" WHERE "core_user"."username" = \'mark48\'  LIMIT 1',
        'INSERT INTO "core_user" ("created_at", "modified_at", "created_by_user_id", "id", "username", "first_name", "last_name", "email", "phone", "language", "address", "city", "zip", "is_active", "date_joined", "meta") VALUES (\'2017-05-21T00:00:00+00:00\'::timestamptz, \'2017-05-21T00:00:00+00:00\'::timestamptz, NULL, \'04adb4e2-f055-c978-c9bb-101ee1bc5cd4\'::uuid, \'mark48\', \'Amanda\', \'Gallagher\', \'banderson@example.com\', NULL, \'en\', NULL, NULL, NULL, true, \'2017-05-21T00:00:00+00:00\'::timestamptz, \'{}\')',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" = \'04adb4e2-f055-c978-c9bb-101ee1bc5cd4\'::uuid',
    ],
    "request": {
        "CONTENT_LENGTH": "533",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/users",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "POST",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "address": None,
                "city": None,
                "created-at": "2017-05-21T00:00:00Z",
                "date-joined": "2017-05-21T00:00:00Z",
                "email": "banderson@example.com",
                "first-name": "Amanda",
                "is-active": True,
                "language": "en",
                "last-name": "Gallagher",
                "meta": {},
                "modified-at": "2017-05-21T00:00:00Z",
                "phone": None,
                "username": "mark48",
                "zip": None,
            },
            "id": "04adb4e2-f055-c978-c9bb-101ee1bc5cd4",
            "relationships": {
                "acls": {"data": [], "meta": {"count": 0}},
                "created-by-user": {"data": None},
            },
            "type": "users",
        }
    },
    "status": 201,
}

snapshots["test_api_patch[ACLViewSet] 1"] = {
    "queries": [
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."id" = \'f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad\'::uuid',
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user" WHERE "core_user"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."id" = \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid',
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" WHERE "core_role"."slug" = \'industry-call\'',
        'SELECT (1) AS "a" FROM "core_acl" WHERE ("core_acl"."role_id" = \'industry-call\' AND "core_acl"."scope_id" = \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid AND "core_acl"."user_id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid AND NOT ("core_acl"."id" = \'f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad\'::uuid))  LIMIT 1',
        'UPDATE "core_acl" SET "created_at" = \'2017-05-21T00:00:00+00:00\'::timestamptz, "modified_at" = \'2017-05-21T00:00:00+00:00\'::timestamptz, "created_by_user_id" = NULL, "user_id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid, "scope_id" = \'9336ebf2-5087-d91c-818e-e6e9ec29f8c1\'::uuid, "role_id" = \'industry-call\' WHERE "core_acl"."id" = \'f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad\'::uuid',
    ],
    "request": {
        "CONTENT_LENGTH": "416",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/acls/f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "PATCH",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "modified-at": "2017-05-21T00:00:00Z",
            },
            "id": "f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
            "relationships": {
                "created-by-user": {"data": None},
                "role": {"data": {"id": "industry-call", "type": "roles"}},
                "scope": {
                    "data": {
                        "id": "9336ebf2-5087-d91c-818e-e6e9ec29f8c1",
                        "type": "scopes",
                    }
                },
                "user": {
                    "data": {
                        "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
                        "type": "users",
                    }
                },
            },
            "type": "acls",
        }
    },
    "status": 200,
}

snapshots["test_api_patch[PermissionViewSet] 1"] = {
    "queries": [
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" WHERE "core_permission"."slug" = \'mrs-shake-recent\'',
        'SELECT (1) AS "a" FROM "core_permission" WHERE ("core_permission"."slug" = \'mrs-shake-recent\' AND NOT ("core_permission"."slug" = \'mrs-shake-recent\'))  LIMIT 1',
        "UPDATE \"core_permission\" SET \"created_at\" = '2017-05-21T00:00:00+00:00'::timestamptz, \"modified_at\" = '2017-05-21T00:00:00+00:00'::timestamptz, \"created_by_user_id\" = NULL, \"name\" = hstore(ARRAY['en','de','fr'], ARRAY['Jordan Mccarthy','','']), \"description\" = hstore(ARRAY['en','de','fr'], ARRAY['Bit among again across environment long line. Team suggest traditional boy above.','','']) WHERE \"core_permission\".\"slug\" = 'mrs-shake-recent'",
    ],
    "request": {
        "CONTENT_LENGTH": "388",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/permissions/mrs-shake-recent",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "PATCH",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": "Bit among again across environment long line. Team suggest traditional boy above.",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Jordan Mccarthy", "fr": ""},
                "slug": "mrs-shake-recent",
            },
            "id": "mrs-shake-recent",
            "relationships": {"created-by-user": {"data": None}},
            "type": "permissions",
        }
    },
    "status": 200,
}

snapshots["test_api_patch[RoleViewSet] 1"] = {
    "queries": [
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" WHERE "core_role"."slug" = \'mrs-shake-recent\'',
        'SELECT (1) AS "a" FROM "core_role" WHERE ("core_role"."slug" = \'mrs-shake-recent\' AND NOT ("core_role"."slug" = \'mrs-shake-recent\'))  LIMIT 1',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" WHERE "core_permission"."slug" = \'rather-cost-admit\'',
        "UPDATE \"core_role\" SET \"created_at\" = '2017-05-21T00:00:00+00:00'::timestamptz, \"modified_at\" = '2017-05-21T00:00:00+00:00'::timestamptz, \"created_by_user_id\" = NULL, \"name\" = hstore(ARRAY['en','de','fr'], ARRAY['Jordan Mccarthy','','']), \"description\" = hstore(ARRAY['en','de','fr'], ARRAY['Bit among again across environment long line. Team suggest traditional boy above.','','']) WHERE \"core_role\".\"slug\" = 'mrs-shake-recent'",
        'SELECT "core_permission"."slug" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'mrs-shake-recent\'',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" INNER JOIN "core_role_permissions" ON ("core_permission"."slug" = "core_role_permissions"."permission_id") WHERE "core_role_permissions"."role_id" = \'mrs-shake-recent\'',
    ],
    "request": {
        "CONTENT_LENGTH": "474",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/roles/mrs-shake-recent",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "PATCH",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": "Bit among again across environment long line. Team suggest traditional boy above.",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Jordan Mccarthy", "fr": ""},
                "slug": "mrs-shake-recent",
            },
            "id": "mrs-shake-recent",
            "relationships": {
                "created-by-user": {"data": None},
                "permissions": {
                    "data": [{"id": "rather-cost-admit", "type": "permissions"}],
                    "meta": {"count": 1},
                },
            },
            "type": "roles",
        }
    },
    "status": 200,
}

snapshots["test_api_patch[ScopeViewSet] 1"] = {
    "queries": [
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        """UPDATE "core_scope" SET "created_at" = \'2017-05-21T00:00:00+00:00\'::timestamptz, "modified_at" = \'2017-05-21T00:00:00+00:00\'::timestamptz, "created_by_user_id" = NULL, "name" = hstore(ARRAY[\'en\',\'de\',\'fr\'], ARRAY[\'Pamela Horton\',\'\',\'\']), "description" = hstore(ARRAY[\'en\',\'de\',\'fr\'], ARRAY[\'Effort meet relationship far. Option program interesting station. First where during teach country talk across.
Argue move appear catch toward help wind. Material minute ago get.\',\'\',\'\']), "parent_id" = NULL WHERE "core_scope"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid""",
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
    ],
    "request": {
        "CONTENT_LENGTH": "534",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/scopes/9dd4e461-268c-8034-f5c8-564e155c67a6",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "PATCH",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "created-at": "2017-05-21T00:00:00Z",
                "description": {
                    "de": "",
                    "en": """Effort meet relationship far. Option program interesting station. First where during teach country talk across.
Argue move appear catch toward help wind. Material minute ago get.""",
                    "fr": "",
                },
                "modified-at": "2017-05-21T00:00:00Z",
                "name": {"de": "", "en": "Pamela Horton", "fr": ""},
            },
            "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
            "relationships": {
                "acls": {"data": [], "meta": {"count": 0}},
                "created-by-user": {"data": None},
                "parent": {"data": None},
            },
            "type": "scopes",
        }
    },
    "status": 200,
}

snapshots["test_api_patch[UserViewSet] 1"] = {
    "queries": [
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user" WHERE "core_user"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT (1) AS "a" FROM "core_user" WHERE ("core_user"."username" = \'mark48\' AND NOT ("core_user"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid))  LIMIT 1',
        'UPDATE "core_user" SET "created_at" = \'2017-05-21T00:00:00+00:00\'::timestamptz, "modified_at" = \'2017-05-21T00:00:00+00:00\'::timestamptz, "created_by_user_id" = NULL, "username" = \'mark48\', "first_name" = \'Amanda\', "last_name" = \'Gallagher\', "email" = \'banderson@example.com\', "phone" = NULL, "language" = \'en\', "address" = NULL, "city" = NULL, "zip" = NULL, "is_active" = true, "date_joined" = \'2017-05-21T00:00:00+00:00\'::timestamptz, "meta" = \'{}\' WHERE "core_user"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
    ],
    "request": {
        "CONTENT_LENGTH": "533",
        "CONTENT_TYPE": "application/vnd.api+json; charset=None",
        "PATH_INFO": "/api/v1/users/9dd4e461-268c-8034-f5c8-564e155c67a6",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "PATCH",
        "SERVER_PORT": "80",
    },
    "response": {
        "data": {
            "attributes": {
                "address": None,
                "city": None,
                "created-at": "2017-05-21T00:00:00Z",
                "date-joined": "2017-05-21T00:00:00Z",
                "email": "banderson@example.com",
                "first-name": "Amanda",
                "is-active": True,
                "language": "en",
                "last-name": "Gallagher",
                "meta": {},
                "modified-at": "2017-05-21T00:00:00Z",
                "phone": None,
                "username": "mark48",
                "zip": None,
            },
            "id": "9dd4e461-268c-8034-f5c8-564e155c67a6",
            "relationships": {
                "acls": {
                    "data": [
                        {"id": "dad3a37a-a9d5-0688-b515-7698acfd7aee", "type": "acls"}
                    ],
                    "meta": {"count": 1},
                },
                "created-by-user": {"data": None},
            },
            "type": "users",
        }
    },
    "status": 200,
}

snapshots["test_api_destroy[ACLViewSet] 1"] = {
    "queries": [
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."id" = \'f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad\'::uuid',
        'DELETE FROM "core_acl" WHERE "core_acl"."id" IN (\'f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad\'::uuid)',
    ],
    "request": {
        "PATH_INFO": "/api/v1/acls/f561aaf6-ef0b-f14d-4208-bb46a4ccb3ad",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "DELETE",
        "SERVER_PORT": "80",
    },
    "status": 204,
}

snapshots["test_api_destroy[PermissionViewSet] 1"] = {
    "queries": [
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" WHERE "core_permission"."slug" = \'mrs-shake-recent\'',
        'SELECT "core_role_permissions"."id", "core_role_permissions"."role_id", "core_role_permissions"."permission_id" FROM "core_role_permissions" WHERE "core_role_permissions"."permission_id" IN (\'mrs-shake-recent\')',
        'DELETE FROM "core_permission" WHERE "core_permission"."slug" IN (\'mrs-shake-recent\')',
    ],
    "request": {
        "PATH_INFO": "/api/v1/permissions/mrs-shake-recent",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "DELETE",
        "SERVER_PORT": "80",
    },
    "status": 204,
}

snapshots["test_api_destroy[RoleViewSet] 1"] = {
    "queries": [
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" WHERE "core_role"."slug" = \'mrs-shake-recent\'',
        'SELECT "core_role_permissions"."id", "core_role_permissions"."role_id", "core_role_permissions"."permission_id" FROM "core_role_permissions" WHERE "core_role_permissions"."role_id" IN (\'mrs-shake-recent\')',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."role_id" IN (\'mrs-shake-recent\')',
        'DELETE FROM "core_role_permissions" WHERE "core_role_permissions"."id" IN (1)',
        'DELETE FROM "core_role" WHERE "core_role"."slug" IN (\'mrs-shake-recent\')',
    ],
    "request": {
        "PATH_INFO": "/api/v1/roles/mrs-shake-recent",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "DELETE",
        "SERVER_PORT": "80",
    },
    "status": 204,
}

snapshots["test_api_destroy[ScopeViewSet] 1"] = {
    "queries": [
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_scope"."id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id" FROM "core_scope" WHERE "core_scope"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        """
            UPDATE "core_scope"
            SET "lft" = CASE
                    WHEN "lft" > 2
                        THEN "lft" +  -2
                    ELSE "lft" END,
                "rght" = CASE
                    WHEN "rght" > 2
                        THEN "rght" +  -2
                    ELSE "rght" END
            WHERE "tree_id" = 1
              AND ("lft" > 2 OR "rght" > 2)""",
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."parent_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."scope_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
        'DELETE FROM "core_scope" WHERE "core_scope"."id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
    ],
    "request": {
        "PATH_INFO": "/api/v1/scopes/9dd4e461-268c-8034-f5c8-564e155c67a6",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "DELETE",
        "SERVER_PORT": "80",
    },
    "status": 204,
}

snapshots["test_api_destroy[UserViewSet] 1"] = {
    "queries": [
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user" WHERE "core_user"."id" = \'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid',
        'SELECT "core_user"."created_at", "core_user"."modified_at", "core_user"."created_by_user_id", "core_user"."id", "core_user"."username", "core_user"."first_name", "core_user"."last_name", "core_user"."email", "core_user"."phone", "core_user"."language", "core_user"."address", "core_user"."city", "core_user"."zip", "core_user"."is_active", "core_user"."date_joined", "core_user"."meta" FROM "core_user" WHERE "core_user"."created_by_user_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
        'SELECT "core_scope"."created_at", "core_scope"."modified_at", "core_scope"."created_by_user_id", "core_scope"."id", "core_scope"."name", "core_scope"."description", "core_scope"."parent_id", "core_scope"."lft", "core_scope"."rght", "core_scope"."tree_id", "core_scope"."level" FROM "core_scope" WHERE "core_scope"."created_by_user_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
        'SELECT "core_role"."created_at", "core_role"."modified_at", "core_role"."created_by_user_id", "core_role"."slug", "core_role"."name", "core_role"."description" FROM "core_role" WHERE "core_role"."created_by_user_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid) ORDER BY "core_role"."slug" ASC',
        'SELECT "core_permission"."created_at", "core_permission"."modified_at", "core_permission"."created_by_user_id", "core_permission"."slug", "core_permission"."name", "core_permission"."description" FROM "core_permission" WHERE "core_permission"."created_by_user_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."created_by_user_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
        'SELECT "core_acl"."created_at", "core_acl"."modified_at", "core_acl"."created_by_user_id", "core_acl"."id", "core_acl"."user_id", "core_acl"."scope_id", "core_acl"."role_id" FROM "core_acl" WHERE "core_acl"."user_id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
        'DELETE FROM "core_acl" WHERE "core_acl"."id" IN (\'dad3a37a-a9d5-0688-b515-7698acfd7aee\'::uuid)',
        'DELETE FROM "core_user" WHERE "core_user"."id" IN (\'9dd4e461-268c-8034-f5c8-564e155c67a6\'::uuid)',
    ],
    "request": {
        "PATH_INFO": "/api/v1/users/9dd4e461-268c-8034-f5c8-564e155c67a6",
        "QUERY_STRING": "",
        "REQUEST_METHOD": "DELETE",
        "SERVER_PORT": "80",
    },
    "status": 204,
}
