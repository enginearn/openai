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
# If you got an error, try this.
openai api models.list
```

``` PowerShell
openai --api-key <OPENAI_API_KEY> api fine_tunes.create -t "[yourfilelocationhere]" -m [modelhere] --suffix "[optional]"
```

[Issue with OpenAI API key while using it in Windows](https://stackoverflow.com/questions/72644231/issue-with-openai-api-key-while-using-it-in-windows)

- `curl`

``` curl PowerShell
$env:OPENAI_API_KEY="YOUR_API_KEY"
curl https://api.openai.com/v1/models -H "Authorization: Bearer $env:OPENAI_API_KEY" | jq '.data[].id'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 43017  100 43017    0     0  73537      0 --:--:-- --:--:-- --:--:-- 73785
"babbage"
"davinci"
"text-davinci-edit-001"
"babbage-code-search-code"
"text-similarity-babbage-001"
"code-davinci-edit-001"
"text-davinci-001"
"ada"
```

- `PowerShell`

``` PowerShell
$headers = @{"Authorization" = "Bearer $env:OPENAI_API_KEY"}
$response = Invoke-RestMethod -Uri $apiUrl -Headers $headers -Method Get
$response.data | ForEach-Object { $_.id }
davinci
text-davinci-edit-001
babbage-code-search-code
text-similarity-babbage-001
code-davinci-edit-001
text-davinci-001
ada
```

[openai api-reference](https://platform.openai.com/docs/api-reference/models)

## Useful prompt?

``` PowerShell
openai api completions.create -m davinci -p "The following is a list of the top 10 most popular programming languages in 2021:" -t "\n1. Python\n2. Java\n3. JavaScript\n4. C#\n5. C++\n6. PHP\n7. R\n8. Objective-C\n9. Swift\n10. TypeScript\n" --stream
```

- openaiが提供しているモデルにはどのような種類がありますか？
- μCARPの具体的な利用方法のサンプルをいくつか教えてください。

---

## References

[OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
