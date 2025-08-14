<script lang="ts">
    
    import papa from 'papaparse';
	import { onMount } from 'svelte';
	import { parse } from 'svelte/compiler';
    let countries: Array<string> = [];
    let selected = null;

    onMount(async() => {
        const res = await fetch('/flags_dataset/dataset.csv');
        const text = await res.text();
        const parsed = papa.parse(text, {header: true});
        countries = parsed.data;
    });

    
    let dataset: string = "/flags_dataset/Flags/";
    let answer = $state("");

    
    const randomFlag = () => {
        const idx = Math.floor(Math.random()*countries.length);
        selected = countries[idx];
    }
</script>

<div class="app">
    <div class="container">
        <div class="heading">
            Guess The Flag!
        </div>

        <div class="flag">
            <img src="{dataset+"ad.png"}" alt="1" />
        </div>

        <div class="options">
            <label for="input">Answer</label>
            <input type="text" bind:value={answer} id="input" />
        </div>

        <div class="next">
            <button class="nextButton">Next</button>

            <button onclick={() => console.log(countries)}>Here</button>
        </div>
    </div>
</div>



<style>
    .app {
        display: flex;
        align-items: center;
        align-self: center;
        justify-content: center;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>