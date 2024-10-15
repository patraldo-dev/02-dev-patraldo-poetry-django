<script>
	import { onMount } from "svelte";

	export let name;
        let src = "./background.png";


	let apimessage = "Waiting for server...";

	onMount(async () => {
		let resp = await fetch("/api/greet").then((res) => res.json());
		console.log(resp);
		apimessage = JSON.stringify(resp);
	});
</script>

<main>
	<h1>¡Hola {name}!</h1>
	<p>
		Visit the <a href="https://dev.to/besil/my-django-svelte-setup-for-fullstack-development-3an8">Django-Svelte setup for fullstack development</a> to learn
		how to build Django-Svelte apps.
	</p>
<img src="/static/frontend/images/background.png" alt="Background image">




	<h3>Data from server</h3>
	{apimessage}
</main>

<style>
        body {
                background-position: center;
        }


	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
