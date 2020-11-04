<script>
    export let tag_name = "Наука";
    export let tag_href = "/science";
</script>

<a href={tag_href} class="tag-href">{tag_name}</a>

<style>
    .tag-href {
        background-color: #282828;
        border-radius: 18px;
        text-align: center;
        padding: 0.375em 0.75em;
        margin-right: 2%;
        margin-left: 0%;
        color: #F9F9F9;
        text-decoration: none;
        margin-top: 2%;
    }
</style>