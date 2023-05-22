RESULT_PLAIN = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

RESULT_TREE = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

RESULT_STAT = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""


RESULT_JSON = """{
    "common": {
        "status": "dict",
        "diff": {
            "follow": {
                "status": "  + ",
                "diff": {
                    "follow": false
                }
            },
            "setting1": {
                "status": "    ",
                "diff": {
                    "setting1": "Value 1"
                }
            },
            "setting2": {
                "status": "  - ",
                "diff": {
                    "setting2": 200
                }
            },
            "setting3": {
                "status": "changed",
                "diff_rem": {
                    "setting3": true
                },
                "diff_add": {
                    "setting3": null
                }
            },
            "setting4": {
                "status": "  + ",
                "diff": {
                    "setting4": "blah blah"
                }
            },
            "setting5": {
                "status": "  + ",
                "diff": {
                    "setting5": {
                        "key5": "value5"
                    }
                }
            },
            "setting6": {
                "status": "dict",
                "diff": {
                    "doge": {
                        "status": "dict",
                        "diff": {
                            "wow": {
                                "status": "changed",
                                "diff_rem": {
                                    "wow": ""
                                },
                                "diff_add": {
                                    "wow": "so much"
                                }
                            }
                        }
                    },
                    "key": {
                        "status": "    ",
                        "diff": {
                            "key": "value"
                        }
                    },
                    "ops": {
                        "status": "  + ",
                        "diff": {
                            "ops": "vops"
                        }
                    }
                }
            }
        }
    },
    "group1": {
        "status": "dict",
        "diff": {
            "baz": {
                "status": "changed",
                "diff_rem": {
                    "baz": "bas"
                },
                "diff_add": {
                    "baz": "bars"
                }
            },
            "foo": {
                "status": "    ",
                "diff": {
                    "foo": "bar"
                }
            },
            "nest": {
                "status": "changed",
                "diff_rem": {
                    "nest": {
                        "key": "value"
                    }
                },
                "diff_add": {
                    "nest": "str"
                }
            }
        }
    },
    "group2": {
        "status": "  - ",
        "diff": {
            "group2": {
                "abc": 12345,
                "deep": {
                    "id": 45
                }
            }
        }
    },
    "group3": {
        "status": "  + ",
        "diff": {
            "group3": {
                "deep": {
                    "id": {
                        "number": 45
                    }
                },
                "fee": 100500
            }
        }
    }
}"""