# OpenAI

## Create API keys

[OpenAI API Keys](https://platform.openai.com/account/api-keys)

## Command line interface

``` PowerShell
$env:OPENAI_API_KEY="YOUR_API_KEY"
```

``` PowerShell
openai --api-key ${OPENAI_API_KEY} api models.list
openai -k ${OPENAI_API_KEY} api models.list
```

``` PowerShell
openai --api-key <OPENAI_API_KEY> api fine_tunes.create -t "[yourfilelocationhere]" -m [modelhere] --suffix "[optional]"
```

[Issue with OpenAI API key while using it in Windows](https://stackoverflow.com/questions/72644231/issue-with-openai-api-key-while-using-it-in-windows)

---

## References

[OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
