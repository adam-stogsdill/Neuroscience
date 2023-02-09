
# Neuroscience
A place for me to place code samples and information related to neuroscience.

I will be storing notes in here about content related to whatever I'm studying at the time in hope to have a repository that maintains all I have learned.

Below using Obsidian's Dataview Plugin, you should be able to see the progress I have made in each book by chapter.

```dataview
TABLE length(filter(file.tasks, (t) => t.completed)) as "Completed", length(filter(file.tasks, (t) => !t.completed)) AS "Uncompleted", length(filter(file.tasks, (t) => t.completed))/ length(filter(file.tasks, (t) => !t.completed)) * 100 as "Percent Complete" WHERE file.tasks AND length(file.tasks) > 0 AND length(filter(file.tasks, (t) => !t.completed)) > 0
```
