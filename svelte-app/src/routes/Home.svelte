<script>
    import { onMount } from 'svelte';
    import axios from 'axios';

    let items = [];

    onMount(async () => {
        const response = await axios.get('http://localhost:8000/api/items/');
        items = response.data;
    });
</script>

<h1>Items</h1>
<ul>
    {#each items as item}
        <li>{item.name}: {item.description}</li>
    {/each}
</ul>
