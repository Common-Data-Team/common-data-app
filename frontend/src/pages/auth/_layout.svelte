<script>
    import {goto, url} from "@sveltech/routify";
    import {checkStoreAndCoockie, user, selfUrl} from "../_api.js";

    // $: if (!checkStoreAndCoockie()) $goto("./auth/signup", {}, false);
    // $goto(selfUrl, {}, false);
    // function logout() {
    //     $user = "";
    // }
</script>

<div>
    <slot/>
</div>
<style>

</style>