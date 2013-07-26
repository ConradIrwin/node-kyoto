{
  "targets": [
    {
      "target_name" : "_kyoto",
      "sources"     : [ "src/_kyoto.cc" ],
      "cflags_cc"   : [ "-fexceptions" ],
      "libraries"   : [ "-lkyotocabinet" ],

      "conditions"  : [
        [ 'OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
          },
        }]
      ]
    }
  ]
}
