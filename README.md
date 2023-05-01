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

## Useful prompt?

``` PowerShell
openai api completions.create -m davinci -p "The following is a list of the top 10 most popular programming languages in 2021:" -t "\n1. Python\n2. Java\n3. JavaScript\n4. C#\n5. C++\n6. PHP\n7. R\n8. Objective-C\n9. Swift\n10. TypeScript\n" --stream
```

- openaiが提供しているモデルにはどのような種類がありますか？
- μCARPの具体的な利用方法のサンプルをいくつか教えてください。

---

## References

[OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
