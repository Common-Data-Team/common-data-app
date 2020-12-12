import {authorizedRequest, dataStore} from "../../../_api";
import {get} from "svelte/store";

export async function EditProject(project_link) {
  let {title, participants_target, questionnaire, markdown, description, project_img, tags} = get(dataStore);
  const response = await authorizedRequest('projects/' + project_link + '/edit', 'PUT',
    {title, participants_target, questionnaire, markdown, description, project_img, tags});
}