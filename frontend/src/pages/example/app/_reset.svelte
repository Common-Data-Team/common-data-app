<script>
    import {goto, url} from "@sveltech/routify";
    import {checkStoreAndCoockie, user} from "./_api";

    /** We set the static parameter to true since we don't want to change the browser's URL
     *  Notice the $: prefix which makes the statement reactive. This way if the user logs
     *  out the $goto is called again.
     * **/
    $: if (!checkStoreAndCoockie()) $goto("./auth/signup", {}, false);
    // $goto("./auth/signup", {}, false);
    function logout() {
        $user = "";
    }
</script>

<slot>
</slot>
