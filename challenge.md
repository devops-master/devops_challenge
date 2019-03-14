# Python Programming Exercise

Please use the provided pom.xml and create a Python script that
customizes the project pom version to match this pattern:
```
<version>ci_{GitHub Org Name Here}_{Branch Name Here -SNAPSHOT</version>
```

The script you write will take three parameters: the path of the pom
file, the GitHub organization name, and the branch name.

As an example, when this script runs on code that lives in the
`Team_Foo` GitHub organization on a branch named `Bar`, the resulting
version would be `ci_Team_Foo_Bar-SNAPSHOT`.

## Python Script Requirements

* It must validate that the pom is syntactically correct
* It must confirm that the existing version is a Maven snapshot
  version prior to making any changes
* The resulting pom version needs to match the format given above
* Unit tests are an added bonus
* Execution within a Docker container is an added bonus

Please provide details on how to execute your solution, as well as any
assumptions/issues/etc. that you feel are appropriate for the reviewer
to be aware of.
